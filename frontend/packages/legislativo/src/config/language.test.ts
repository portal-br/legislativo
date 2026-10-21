import type { ConfigType } from '@plone/registry';
import { describe, expect, it } from 'vitest';
import {
  getSupportedLocales,
  negotiateLocale,
  resolveContentLocale,
} from '@plone/volto/helpers/Locale/Locale';
import install from './settings';

// O SSR do Volto escolhe o idioma da interface com estes helpers, a partir
// do cookie I18N_LANGUAGE ou do cabeçalho Accept-Language do navegador.
// O Portal Modelo é monolíngue em português: nenhuma preferência do
// visitante pode levar a página a ser renderizada em outro idioma.

const makeConfig = () =>
  ({
    settings: {
      defaultLanguage: 'en',
      supportedLanguages: ['en', 'pt-br'],
      appExtras: [],
    },
  }) as unknown as ConfigType;

const supported = getSupportedLocales(
  install(makeConfig()).settings.supportedLanguages,
);

describe('idioma da renderização no servidor', () => {
  it.each([
    'en-US,en;q=0.9',
    'en',
    'es-ES,es;q=0.8',
    'de',
    'pt-BR,pt;q=0.9,en;q=0.8',
    'pt-br',
    '',
    null,
    undefined,
  ])('renderiza em português para a preferência %j', (preference) => {
    expect(negotiateLocale(preference, supported)).toBe('pt-BR');
  });

  it('não troca de idioma em conteúdo em português', () => {
    expect(resolveContentLocale('pt-br', ['pt-BR'], supported)).toBeNull();
  });

  it('troca para português quando a requisição veio em outro idioma', () => {
    expect(resolveContentLocale('pt-br', ['en'], supported)).toBe('pt-BR');
  });

  it('seguiria o navegador se o inglês continuasse suportado', () => {
    const multilingual = getSupportedLocales(
      makeConfig().settings.supportedLanguages,
    );
    expect(negotiateLocale('en-US,en;q=0.9', multilingual)).toBe('en');
  });

  it('mantém português em conteúdo marcado com outro idioma', () => {
    expect(resolveContentLocale('en', ['pt-BR'], supported)).toBeNull();
  });
});
