import { defineConfig } from 'vitest/config';
import voltoVitestConfig from '@plone/volto/vitest.config.mjs';
import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);

// Volto add-ons ship their sources in `src/`; webpack aliases the package
// name to that folder, so tests need the same aliases.
const addonSrc = (name) =>
  path.join(path.dirname(require.resolve(`${name}/package.json`)), 'src');

const aliases = {
  '@plone/volto': path.resolve(__dirname, '../../core/packages/volto/src'), // Add paths accordingly
  '@portalbrasil/legislativo': path.resolve(__dirname, './src'), // Add paths accordingly
  '@eeacms/volto-pdf-block': addonSrc('@eeacms/volto-pdf-block'),
  '@plonegovbr/volto-vlibras': addonSrc('@plonegovbr/volto-vlibras'),
};

// Each Volto test project declares its own aliases, which take precedence
// over the top-level ones, so ours are merged into every project.
const projects = voltoVitestConfig.test.projects.map((project) => ({
  ...project,
  resolve: {
    ...project.resolve,
    alias: { ...project.resolve?.alias, ...aliases },
  },
}));

export default defineConfig({
  ...voltoVitestConfig,
  resolve: {
    alias: aliases,
  },
  test: {
    ...voltoVitestConfig.test,
    projects,
  },
});
