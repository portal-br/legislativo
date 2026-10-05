import { createIntl } from 'react-intl';
import { afterEach, describe, expect, it } from 'vitest';
import config from '@plone/volto/registry';
import { buttonSchema, ICON_CHOICES, multiButtonsSchema } from './schema';

const intl = createIntl({ locale: 'en', messages: {} });
const originalThemes = config.blocks.themes;

afterEach(() => {
  config.blocks.themes = originalThemes;
});

describe('buttonSchema', () => {
  it.each([
    ['default', ['title', 'href', 'icon', 'openInNewTab']],
    ['card', ['title', 'description', 'href', 'openInNewTab']],
    ['image', ['title', 'image', 'altText', 'href', 'openInNewTab']],
  ] as const)('mostra os campos da variação %s', (variant, fields) => {
    expect(buttonSchema(intl, variant).fieldsets[0].fields).toEqual(fields);
  });

  it('exige imagem e texto alternativo na variação de imagens', () => {
    expect(buttonSchema(intl, 'image').required).toEqual(['image', 'altText']);
    expect(buttonSchema(intl, 'default').required).toEqual([]);
  });

  it('usa um rótulo para leitores de tela na variação de imagens', () => {
    expect(buttonSchema(intl, 'image').properties.title.title).toBe(
      'Label for screen readers',
    );
    expect(buttonSchema(intl, 'card').properties.title.title).toBe('Label');
  });

  it('oferece os ícones conhecidos', () => {
    const { choices } = buttonSchema(intl, 'default').properties.icon;
    expect(choices.map(([name]: [string]) => name)).toEqual(
      ICON_CHOICES.map(([name]) => name),
    );
  });
});

describe('multiButtonsSchema', () => {
  it('monta os campos do bloco', () => {
    const schema = multiButtonsSchema({ intl });
    expect(schema.title).toBe('Multiple buttons');
    expect(schema.fieldsets[0].fields).toEqual([
      'variant',
      'buttons',
      'maxColumns',
      'stretch',
      'theme',
    ]);
  });

  it('usa a variação dos dados do bloco nos botões', () => {
    const schema = multiButtonsSchema({ intl, data: { variant: 'card' } });
    expect(schema.properties.buttons.schema.fieldsets[0].fields).toContain(
      'description',
    );
  });

  it('aceita os dados em formData', () => {
    const schema = multiButtonsSchema({ intl, formData: { variant: 'image' } });
    expect(schema.properties.buttons.schema.required).toEqual([
      'image',
      'altText',
    ]);
  });

  it('usa a variação de botões por padrão', () => {
    const schema = multiButtonsSchema({ intl, data: {} });
    expect(schema.properties.buttons.schema.fieldsets[0].fields).toContain(
      'icon',
    );
  });

  it('oferece os temas de bloco, com o primeiro como padrão', () => {
    const themes = [
      { name: 'default', label: 'Primary', style: {} },
      { name: 'brand', label: 'Brand', style: {} },
    ];
    config.blocks.themes = themes;
    const { theme } = multiButtonsSchema({ intl }).properties;
    expect(theme.themes).toBe(themes);
    expect(theme.default).toBe('default');
  });

  it('funciona sem temas de bloco', () => {
    config.blocks.themes = undefined as unknown as typeof originalThemes;
    const { theme } = multiButtonsSchema({ intl }).properties;
    expect(theme.themes).toEqual([]);
    expect(theme.default).toBeUndefined();
  });
});
