import { readFileSync } from 'fs';
import { createRequire } from 'module';
import path from 'path';
import { createIntl } from 'react-intl';
import { describe, expect, it } from 'vitest';
import { buttonSchema, multiButtonsSchema } from './schema';

// The same loader that the Volto build uses to collect the block docs.
const require = createRequire(import.meta.url);
const { findBlocksDocs } = require('@plone/registry/create-blocks-docs-loader');

const intl = createIntl({ locale: 'en', messages: {} });
const SRC_DIR = path.resolve(__dirname, '..', '..', '..');
const DOCS_FILE = path.join(__dirname, 'docs.block.md');

/** Extrai o primeiro bloco ```json do arquivo de documentação. */
const docsExample = (): Record<string, any> => {
  const markdown = readFileSync(DOCS_FILE, 'utf-8');
  const json = markdown.match(/```json\n([\s\S]*?)\n```/)?.[1];
  return JSON.parse(json ?? 'null');
};

describe('documentação do bloco multiButtons', () => {
  it('é coletada pelo build como documentação de multiButtons', () => {
    const found = findBlocksDocs([SRC_DIR]).find(
      (source) => source.block === 'multiButtons',
    );
    expect(found?.path).toBe(DOCS_FILE);
    expect(found?.variation).toBeUndefined();
  });

  it('tem um exemplo completo com o @type do bloco', () => {
    const example = docsExample();
    expect(example['@type']).toBe('multiButtons');
    expect(example.buttons.length).toBeGreaterThan(0);
  });

  it('o exemplo só usa campos que o schema do bloco define', () => {
    const example = docsExample();
    const { properties } = multiButtonsSchema({ intl, data: example });
    for (const key of Object.keys(example)) {
      if (key === '@type') continue;
      expect(properties).toHaveProperty(key);
    }
  });

  it('os botões do exemplo usam campos da variação dele', () => {
    const example = docsExample();
    const variant = example.variant ?? 'default';
    const { properties } = buttonSchema(intl, variant);
    for (const button of example.buttons) {
      for (const key of Object.keys(button)) {
        if (key === '@id') continue;
        expect(properties).toHaveProperty(key);
      }
    }
  });
});

describe('schema do endpoint @blocks-schema', () => {
  it('monta o schema só com intl e o @type, como o endpoint chama', () => {
    const schema = multiButtonsSchema({
      intl,
      data: { '@type': 'multiButtons' },
    });
    expect(schema.title).toBe('Multiple buttons');
    expect(schema.properties.variant.choices).toHaveLength(3);
    expect(schema.properties.buttons.schema.fieldsets[0].fields).toContain(
      'icon',
    );
  });
});
