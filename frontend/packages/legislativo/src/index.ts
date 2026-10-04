import type { ConfigType } from '@plone/registry';
import installSettings from './config/settings';
import installViews from './config/views';

function applyConfig(config: ConfigType) {
  installSettings(config);
  installViews(config);

  return config;
}

export default applyConfig;
