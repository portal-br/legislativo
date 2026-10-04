import { describe, expect, it } from 'vitest';
import config from '@plone/volto/registry';
import {
  accessibleLabel,
  columns,
  firstTarget,
  imageSrc,
  targetURL,
  themeStyle,
} from './helpers';

const THEMES = [
  { name: 'default', style: { '--theme-color': 'white' } },
  { name: 'brand', style: { '--theme-color': 'blue' } },
];

describe('firstTarget', () => {
  it('usa o primeiro item do object_browser', () => {
    expect(firstTarget([{ '@id': '/a' }, { '@id': '/b' }])).toEqual({
      '@id': '/a',
    });
  });

  it('aceita uma URL digitada', () => {
    expect(firstTarget('  https://example.org  ')).toEqual({
      '@id': 'https://example.org',
    });
  });

  it.each([[undefined], [''], ['   '], [[]]])(
    'ignora campo vazio (%j)',
    (v) => {
      expect(firstTarget(v)).toBeUndefined();
    },
  );
});

describe('targetURL', () => {
  it('devolve o endereço do alvo', () => {
    expect(targetURL([{ '@id': '/noticias' }])).toBe('/noticias');
  });

  it('ignora alvo sem endereço', () => {
    expect(targetURL([{ title: 'Sem endereço' }])).toBeUndefined();
    expect(targetURL(undefined)).toBeUndefined();
  });
});

describe('imageSrc', () => {
  const api = () => config.settings.apiPath;

  it('usa a escala padrão de imagens internas', () => {
    expect(imageSrc(`${api()}/imagens/foto/`)).toBe(
      '/imagens/foto/@@images/image',
    );
  });

  it('preserva endereços de escala já resolvidos', () => {
    expect(imageSrc(`${api()}/imagens/foto/@@images/image/large`)).toBe(
      '/imagens/foto/@@images/image/large',
    );
  });

  it('não altera imagens externas', () => {
    expect(imageSrc('https://example.org/foto.png')).toBe(
      'https://example.org/foto.png',
    );
  });
});

describe('accessibleLabel', () => {
  it('prefere o texto alternativo', () => {
    expect(
      accessibleLabel({ altText: 'Portal da transparência', title: 'T' }),
    ).toBe('Portal da transparência');
  });

  it('usa o título e depois a descrição', () => {
    expect(accessibleLabel({ title: ' Ouvidoria ' })).toBe('Ouvidoria');
    expect(accessibleLabel({ description: 'Fale conosco' })).toBe(
      'Fale conosco',
    );
  });

  it.each([['https://example.org'], ['/pagina'], ['']])(
    'recusa endereços e textos vazios (%j)',
    (title) => {
      expect(accessibleLabel({ title })).toBeUndefined();
    },
  );
});

describe('columns', () => {
  it('limita o máximo ao número de botões', () => {
    expect(columns(4, 2)).toBe(2);
    expect(columns(2, 5)).toBe(2);
  });

  it('arredonda para baixo', () => {
    expect(columns(2.7, 5)).toBe(2);
  });

  it.each([[undefined], [0], [-1], [Number.NaN], [Infinity]])(
    'sem máximo válido (%s) usa um botão por coluna',
    (max) => {
      expect(columns(max, 3)).toBe(3);
    },
  );

  it('tem pelo menos uma coluna', () => {
    expect(columns(3, 0)).toBe(1);
  });
});

describe('themeStyle', () => {
  it('devolve as variáveis do tema escolhido', () => {
    expect(themeStyle({ theme: 'brand' }, THEMES)).toEqual({
      '--theme-color': 'blue',
    });
  });

  it('ignora tema desconhecido ou ausente', () => {
    expect(themeStyle({ theme: 'alt' }, THEMES)).toEqual({});
    expect(themeStyle({}, THEMES)).toEqual({});
  });
});
