import type { ConfigType } from '@plone/registry';
import { describe, expect, it } from 'vitest';
import MultiButtonsBlockInfo from '../components/Blocks/MultiButtons';
import install, { GALERIA_BLOCKS, NEWS_ITEM_BLOCKS } from './blocks';

const OTHER = { id: 'other' };

const makeConfig = (gridBlock?: object) =>
  ({
    blocks: {
      blocksConfig: { other: OTHER, ...(gridBlock ? { gridBlock } : {}) },
    },
  }) as unknown as ConfigType;

describe('install blocks', () => {
  it('registra o bloco de múltiplos botões', () => {
    const { blocks } = install(makeConfig());
    expect(blocks.blocksConfig.multiButtons).toBe(MultiButtonsBlockInfo);
    expect(blocks.blocksConfig.other).toBe(OTHER);
  });

  it('libera o bloco dentro da grade', () => {
    const grid = {
      id: 'gridBlock',
      allowedBlocks: ['slate'],
      blocksConfig: {},
    };
    const config = install(makeConfig(grid));
    const gridBlock = config.blocks.blocksConfig
      .gridBlock as unknown as typeof grid;
    expect(gridBlock.allowedBlocks).toEqual(['slate', 'multiButtons']);
    expect(gridBlock.blocksConfig).toEqual({
      multiButtons: MultiButtonsBlockInfo,
    });
  });

  it('não duplica o bloco na grade', () => {
    const grid = {
      id: 'gridBlock',
      allowedBlocks: ['multiButtons'],
      blocksConfig: {},
    };
    install(makeConfig(grid));
    expect(grid.allowedBlocks).toEqual(['multiButtons']);
  });

  it('ignora grade sem lista de blocos', () => {
    const grid = { id: 'gridBlock' };
    install(makeConfig(grid));
    expect(grid).toEqual({ id: 'gridBlock' });
  });

  it('ignora grade sem configuração de blocos', () => {
    const grid = { id: 'gridBlock', allowedBlocks: ['slate'] };
    install(makeConfig(grid));
    expect(grid.allowedBlocks).toEqual(['slate']);
  });
});

describe('initialBlocks', () => {
  const types = (blocks: Array<{ '@type': string }>) =>
    blocks.map((block) => block['@type']);

  it('começa notícias com título, descrição, imagem principal e texto', () => {
    const { blocks } = install(makeConfig());
    expect(blocks.initialBlocks['News Item']).toBe(NEWS_ITEM_BLOCKS);
    expect(types(NEWS_ITEM_BLOCKS)).toEqual([
      'title',
      'description',
      'mainImageBlock',
      'slate',
    ]);
  });

  it('guarda a largura da imagem principal nos estilos do bloco', () => {
    expect(NEWS_ITEM_BLOCKS[2]).toMatchObject({
      styles: {
        'blockWidth:noprefix': {
          '--block-width': 'var(--default-container-width)',
        },
      },
    });
  });

  it('começa galerias com a listagem das próprias imagens', () => {
    const { blocks } = install(makeConfig());
    expect(blocks.initialBlocks.Galeria).toBe(GALERIA_BLOCKS);
    expect(types(GALERIA_BLOCKS)).toEqual(['title', 'listing', 'slate']);
    expect(GALERIA_BLOCKS[1]).toMatchObject({
      variation: 'imageGallery',
      querystring: {
        query: [
          { i: 'portal_type', v: ['Image'] },
          { i: 'path', v: './' },
        ],
        sort_on: 'getObjPositionInParent',
      },
    });
  });

  it('preserva os blocos iniciais de outros tipos', () => {
    const config = makeConfig();
    const document = [{ '@type': 'title' }];
    config.blocks.initialBlocks = { Document: document };
    expect(install(config).blocks.initialBlocks.Document).toBe(document);
  });
});
