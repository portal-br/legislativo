import { readFileSync } from 'fs';
import { createRequire } from 'module';
import path from 'path';
import { describe, expect, it } from 'vitest';

const require = createRequire(import.meta.url);

const CATALOG = path.join('locales', 'pt_BR', 'LC_MESSAGES', 'volto.po');

/** Lê as mensagens de um catálogo .po, ignorando o cabeçalho. */
const readCatalog = (file: string): Map<string, string> => {
  const source = readFileSync(file, 'utf-8');
  const entries = new Map<string, string>();
  const pattern = /^msgid "(.*)"\nmsgstr "(.*)"$/gm;
  for (const [, msgid, msgstr] of source.matchAll(pattern)) {
    if (msgid) entries.set(msgid, msgstr);
  }
  return entries;
};

const packageCatalog = readCatalog(path.resolve(__dirname, '..', CATALOG));

const themeCatalog = readCatalog(
  path.join(
    path.dirname(
      require.resolve('@simplesconsultoria/volto-light-theme/package.json'),
    ),
    CATALOG,
  ),
);

describe('catálogo pt_BR do Portal Modelo', () => {
  it('tem mensagens', () => {
    expect(packageCatalog.size).toBeGreaterThan(0);
  });

  it('traduz todas as mensagens', () => {
    const missing = [...packageCatalog]
      .filter(([, msgstr]) => !msgstr)
      .map(([msgid]) => msgid);
    expect(missing).toEqual([]);
  });

  it('traduz o título do bloco de múltiplos botões', () => {
    expect(packageCatalog.get('Multiple buttons')).toBe('Múltiplos botões');
  });
});

describe('catálogo pt_BR do tema', () => {
  it.each([
    ['Hero Block', 'Bloco Hero'],
    ['Custom Grid', 'Grade personalizada'],
    ['Event Metadata', 'Metadados do evento'],
  ])('traduz %s', (msgid, expected) => {
    expect(themeCatalog.get(msgid)).toBe(expected);
  });
});
