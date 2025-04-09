import projectPackageJson from '../../package.json';

export default function install(config) {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';
  config.settings.projecName = projectPackageJson.name;
  config.settings.projecVersion = projectPackageJson.version;

  return config;
}
