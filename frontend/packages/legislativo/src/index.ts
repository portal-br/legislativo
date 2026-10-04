import type { ConfigType } from '@plone/registry';
import installBlocks from './config/blocks';
import installSettings from './config/settings';
import installViews from './config/views';

function applyConfig(config: ConfigType) {
  installSettings(config);
  installBlocks(config);
  installViews(config);

  return config;
}

export default applyConfig;
