import type { ConfigType } from '@plone/registry';
import { describe, expect, it } from 'vitest';
import MultiButtonsBlockInfo from '../components/Blocks/MultiButtons';
import install from './blocks';

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
