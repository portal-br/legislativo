import type { ConfigType } from '@plone/registry';
// VLibras
import Libras from '@plonegovbr/volto-vlibras/components/Libras';

export default function install(config: ConfigType) {
  // Idioma em português
  config.settings.isMultilingual = false;
  config.settings.defaultLanguage = 'pt-br';
  // Languages not added to supportedLanguages will not be included in the build
  config.settings.supportedLanguages = ['pt-br'];

  // Habilita VLibras
  config.settings.appExtras = [
    ...config.settings.appExtras,
    {
      match: '',
      component: Libras,
      props: {},
    },
  ];

  return config;
}
