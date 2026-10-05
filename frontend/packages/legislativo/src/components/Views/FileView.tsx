/**
 * FileView view component.
 * @module components/Views/FileView
 */
import { Container } from '@plone/components';
import { flattenToAppURL } from '@plone/volto/helpers/Url/Url';
import PDFBlockView from '@eeacms/volto-pdf-block/components/manage/PDFViewer/BlockView';
import { defineMessages, useIntl } from 'react-intl';
import { formatFileSize } from '../../helpers/fileSize';
import type { ContentTypeViewProps, FileContent } from '../../types';

export const PDF_CONTENT_TYPE = 'application/pdf';

const messages = defineMessages({
  downloadFile: {
    id: 'Download file',
    defaultMessage: 'Download file',
  },
  pdfViewer: {
    id: 'PDF viewer',
    defaultMessage: 'PDF viewer',
  },
});

/**
 * Indica se o conteúdo armazena um arquivo PDF.
 * @param content Conteúdo do tipo Arquivo.
 * @returns `true` quando o tipo MIME do arquivo é PDF.
 */
export function isPDF(content: FileContent): boolean {
  return content.file?.['content-type'] === PDF_CONTENT_TYPE;
}

/**
 * Visão padrão do tipo Arquivo: link para download e, para PDFs,
 * o visualizador do documento.
 * @param content Conteúdo do tipo Arquivo.
 * @returns Markup of the component.
 */
const FileView = (props: ContentTypeViewProps<FileContent>) => {
  const { content } = props;
  const intl = useIntl();
  const file = content.file;

  return (
    <Container narrow id="page-document" className="view-wrapper fileitem-view">
      <h1 className="documentFirstHeading">{content.title}</h1>
      {content.description && (
        <p className="documentDescription">{content.description}</p>
      )}
      {file?.download && (
        <p className="file-download">
          <a href={flattenToAppURL(file.download)}>
            {file.filename || intl.formatMessage(messages.downloadFile)}
          </a>{' '}
          <span className="file-size">({formatFileSize(file.size)})</span>
        </p>
      )}
      {isPDF(content) && (
        <section
          className="file-pdf-viewer"
          aria-label={intl.formatMessage(messages.pdfViewer)}
        >
          <PDFBlockView data={{ url: flattenToAppURL(content['@id']) }} />
        </section>
      )}
    </Container>
  );
};

export default FileView;
