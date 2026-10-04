import type { ComponentType } from 'react';
import Wrapper from '@plone/volto/storybook';
import FileView from './FileView';
import type { FileContent } from '../../types';

const makeContent = (contentType: string, filename: string): FileContent =>
  ({
    '@id': `/documentos/${filename}`,
    '@type': 'File',
    title: 'Relatório anual',
    description: 'Relatório de atividades da câmara',
    file: {
      'content-type': contentType,
      download: `/documentos/${filename}/@@download/file`,
      filename,
      size: 2500000,
    },
  }) as FileContent;

const withWrapper = (Story: ComponentType) => (
  <Wrapper anonymous>
    <div style={{ width: '1000px', backgroundColor: 'white' }}>
      <Story />
    </div>
  </Wrapper>
);

const meta = {
  title: 'Public/Views/FileView',
  component: FileView,
  decorators: [withWrapper],
};

export default meta;

export const ArquivoPDF = {
  args: {
    content: makeContent('application/pdf', 'relatorio.pdf'),
  },
};

export const OutroArquivo = {
  args: {
    content: makeContent('application/msword', 'relatorio.doc'),
  },
};
