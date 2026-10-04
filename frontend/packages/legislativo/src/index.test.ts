import type { ConfigType } from '@plone/registry';
import { describe, expect, it } from 'vitest';
import Libras from '@plonegovbr/volto-vlibras/components/Libras';
import applyConfig from './index';
import FileView from './components/Views/FileView';

const OTHER_VIEW = () => null;
const OTHER_EXTRA = { match: '/outro', component: OTHER_VIEW };

const makeConfig = () =>
  ({
    settings: {
      isMultilingual: true,
      defaultLanguage: 'en',
      supportedLanguages: ['en', 'pt-br'],
      appExtras: [OTHER_EXTRA],
    },
    views: {
      contentTypesViews: { Document: OTHER_VIEW },
    },
  }) as unknown as ConfigType;

describe('applyConfig', () => {
  it('configura o site apenas em português', () => {
    const { settings } = applyConfig(makeConfig());
    expect(settings.isMultilingual).toBe(false);
    expect(settings.defaultLanguage).toBe('pt-br');
    expect(settings.supportedLanguages).toEqual(['pt-br']);
  });

  it('habilita o VLibras em todas as páginas', () => {
    const { settings } = applyConfig(makeConfig());
    expect(settings.appExtras).toEqual([
      OTHER_EXTRA,
      { match: '', component: Libras, props: {} },
    ]);
  });

  it('usa a visão de arquivo do Portal Modelo', () => {
    const { views } = applyConfig(makeConfig());
    expect(views.contentTypesViews.File).toBe(FileView);
  });

  it('preserva as demais visões por tipo', () => {
    const { views } = applyConfig(makeConfig());
    expect(views.contentTypesViews.Document).toBe(OTHER_VIEW);
  });
});
