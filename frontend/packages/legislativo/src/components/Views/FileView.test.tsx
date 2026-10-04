import { render, screen } from '@testing-library/react';
import { IntlProvider } from 'react-intl';
import { describe, expect, it, vi } from 'vitest';
import config from '@plone/volto/registry';
import FileView, { isPDF } from './FileView';
import type { FileContent, NamedFile } from '../../types';

vi.mock(
  '@eeacms/volto-pdf-block/components/manage/PDFViewer/BlockView',
  () => ({
    default: ({ data }: { data: { url: string } }) => (
      <div data-testid="pdf-viewer" data-url={data.url} />
    ),
  }),
);

const apiPath = () => config.settings.apiPath;

const makeFile = (overrides: Partial<NamedFile> = {}): NamedFile => ({
  'content-type': 'application/pdf',
  download: `${apiPath()}/documentos/relatorio.pdf/@@download/file`,
  filename: 'relatorio.pdf',
  size: 2500000,
  ...overrides,
});

const makeContent = (file: NamedFile | null): FileContent =>
  ({
    '@id': `${apiPath()}/documentos/relatorio.pdf`,
    '@type': 'File',
    title: 'Relatório anual',
    description: 'Relatório de atividades da câmara',
    file,
  }) as FileContent;

const renderView = (content: FileContent) =>
  render(
    <IntlProvider locale="pt-br" messages={{}}>
      <FileView content={content} />
    </IntlProvider>,
  );

describe('isPDF', () => {
  it('reconhece arquivos PDF', () => {
    expect(isPDF(makeContent(makeFile()))).toBe(true);
  });

  it('recusa outros tipos de arquivo', () => {
    const file = makeFile({ 'content-type': 'application/msword' });
    expect(isPDF(makeContent(file))).toBe(false);
  });

  it('recusa conteúdo sem arquivo', () => {
    expect(isPDF(makeContent(null))).toBe(false);
  });
});

describe('FileView', () => {
  it('mostra título e descrição', () => {
    renderView(makeContent(makeFile()));
    expect(
      screen.getByRole('heading', { name: 'Relatório anual' }),
    ).toBeInTheDocument();
    expect(
      screen.getByText('Relatório de atividades da câmara'),
    ).toBeInTheDocument();
  });

  it('mostra o link de download com tamanho', () => {
    renderView(makeContent(makeFile()));
    const link = screen.getByRole('link', { name: 'relatorio.pdf' });
    expect(link).toHaveAttribute(
      'href',
      '/documentos/relatorio.pdf/@@download/file',
    );
    expect(screen.getByText('(3 MB)')).toBeInTheDocument();
  });

  it('usa um texto padrão quando o arquivo não tem nome', () => {
    renderView(makeContent(makeFile({ filename: '' })));
    expect(
      screen.getByRole('link', { name: 'Download file' }),
    ).toBeInTheDocument();
  });

  it('mostra o visualizador para PDFs', () => {
    renderView(makeContent(makeFile()));
    expect(screen.getByTestId('pdf-viewer')).toHaveAttribute(
      'data-url',
      '/documentos/relatorio.pdf',
    );
    expect(
      screen.getByRole('region', { name: 'PDF viewer' }),
    ).toBeInTheDocument();
  });

  it('não mostra o visualizador para outros arquivos', () => {
    renderView(makeContent(makeFile({ 'content-type': 'application/msword' })));
    expect(screen.queryByTestId('pdf-viewer')).not.toBeInTheDocument();
  });

  it('não mostra download nem visualizador sem arquivo', () => {
    renderView(makeContent(null));
    expect(screen.queryByRole('link')).not.toBeInTheDocument();
    expect(screen.queryByTestId('pdf-viewer')).not.toBeInTheDocument();
  });
});
