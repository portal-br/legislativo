import type { BlockConfigBase } from '@plone/types';
import type { ConfigType } from '@plone/registry';
import MultiButtonsBlockInfo, {
  BLOCK_ID as MULTI_BUTTONS,
} from '../components/Blocks/MultiButtons';

interface GridBlockConfig extends BlockConfigBase {
  allowedBlocks?: string[];
  blocksConfig?: Record<string, BlockConfigBase>;
}

/**
 * Libera um bloco dentro do bloco de grade, quando a grade existe.
 * @param config Configuração do Volto.
 * @param blockId Id do bloco já registrado em `blocksConfig`.
 */
function allowInGrid(config: ConfigType, blockId: string) {
  const grid = config.blocks.blocksConfig.gridBlock as
    | GridBlockConfig
    | undefined;
  if (!grid?.allowedBlocks || !grid.blocksConfig) return;
  if (!grid.allowedBlocks.includes(blockId)) {
    grid.allowedBlocks = [...grid.allowedBlocks, blockId];
  }
  grid.blocksConfig[blockId] = config.blocks.blocksConfig[blockId];
}

/** Blocos com que uma notícia nova começa: a imagem principal vem da prévia. */
export const NEWS_ITEM_BLOCKS = [
  { '@type': 'title', fixed: true, required: true },
  { '@type': 'description', fixed: true, required: true },
  {
    '@type': 'mainImageBlock',
    align: 'center',
    size: 'l',
    theme: 'default',
    styles: {
      'blockWidth:noprefix': {
        '--block-width': 'var(--default-container-width)',
      },
    },
  },
  { '@type': 'slate' },
];

/** Blocos com que uma galeria nova começa: as imagens dela, na ordem da pasta. */
export const GALERIA_BLOCKS = [
  { '@type': 'title', fixed: true, required: true },
  {
    '@type': 'listing',
    variation: 'imageGallery',
    headlineTag: 'h2',
    theme: 'default',
    styles: {},
    querystring: {
      query: [
        {
          i: 'portal_type',
          o: 'plone.app.querystring.operation.selection.any',
          v: ['Image'],
        },
        {
          i: 'path',
          o: 'plone.app.querystring.operation.string.relativePath',
          v: './',
        },
      ],
      sort_on: 'getObjPositionInParent',
      sort_order: 'ascending',
    },
  },
  { '@type': 'slate' },
];

export default function install(config: ConfigType) {
  config.blocks.blocksConfig[MULTI_BUTTONS] = MultiButtonsBlockInfo;
  allowInGrid(config, MULTI_BUTTONS);

  config.blocks.initialBlocks = {
    ...config.blocks.initialBlocks,
    'News Item': NEWS_ITEM_BLOCKS,
    Galeria: GALERIA_BLOCKS,
  };

  return config;
}
