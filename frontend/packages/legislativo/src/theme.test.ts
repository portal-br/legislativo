import type { ConfigType } from '@plone/registry';
import { beforeAll, describe, expect, it } from 'vitest';
import config from '@plone/volto/registry';
import applyTheme from '@simplesconsultoria/volto-light-theme';
import applyConfig from './index';

// O Portal Modelo usa blocos, variações e componentes que o tema entrega.
// Estes testes aplicam a configuração do tema e a do Portal Modelo sobre o
// registro de teste do Volto e conferem o que o site espera encontrar.
// O registro de teste não tem o bloco de grade nem a configuração do
// @kitconcept/volto-light-theme; a grade é testada em config/blocks.test.ts.

let applied: ConfigType;

beforeAll(() => {
  const base = config as unknown as ConfigType;
  base.settings.appExtras = base.settings.appExtras ?? [];
  applied = applyConfig(applyTheme(base));
});

describe('funcionalidades entregues pelo tema', () => {
  it('registra o bloco de imagem principal usado nas notícias', () => {
    expect(applied.blocks.blocksConfig.mainImageBlock).toBeDefined();
  });

  it.each(['carousel', 'mediaCarousel', 'teaser', 'imageGallery'])(
    'oferece a variação de listagem %s',
    (id) => {
      const variations = applied.blocks.blocksConfig.listing.variations ?? [];
      expect(variations.map((variation) => variation.id)).toContain(id);
    },
  );

  it('define temas de bloco', () => {
    const names = (applied.blocks.themes ?? []).map((theme) => theme.name);
    expect(names).toContain('default');
  });

  it('usa o bloco de imagem principal do tema nas notícias novas', () => {
    const types = applied.blocks.initialBlocks['News Item'].map(
      (block: { '@type': string }) => block['@type'],
    );
    expect(types).toContain('mainImageBlock');
  });
});
