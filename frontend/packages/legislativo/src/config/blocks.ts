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

export default function install(config: ConfigType) {
  config.blocks.blocksConfig[MULTI_BUTTONS] = MultiButtonsBlockInfo;
  allowInGrid(config, MULTI_BUTTONS);

  return config;
}
