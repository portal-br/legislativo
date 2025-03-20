import installSettings from './config/settings';

const applyConfig = (config) => {
  // Instala configurações básicas
  installSettings(config);

  return config;
};

export default applyConfig;
