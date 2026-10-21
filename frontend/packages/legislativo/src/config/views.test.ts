import type { ConfigType } from '@plone/registry';
import { describe, expect, it } from 'vitest';
import FileView from '../components/Views/FileView';
import install from './views';

const OTHER_VIEW = () => null;

const makeConfig = (contentTypesViews: object = {}) =>
  ({
    views: { contentTypesViews },
  }) as unknown as ConfigType;

describe('install views', () => {
  it('usa a visão de arquivo do Portal Modelo', () => {
    const { views } = install(makeConfig());
    expect(views.contentTypesViews.File).toBe(FileView);
  });

  it('substitui a visão de arquivo existente', () => {
    const { views } = install(makeConfig({ File: OTHER_VIEW }));
    expect(views.contentTypesViews.File).toBe(FileView);
  });

  it('preserva as visões dos demais tipos', () => {
    const { views } = install(makeConfig({ Document: OTHER_VIEW }));
    expect(views.contentTypesViews.Document).toBe(OTHER_VIEW);
  });

  it('não altera o objeto de visões recebido', () => {
    const original = { Document: OTHER_VIEW };
    install(makeConfig(original));
    expect(original).toEqual({ Document: OTHER_VIEW });
  });

  it('devolve a mesma configuração', () => {
    const config = makeConfig();
    expect(install(config)).toBe(config);
  });
});
