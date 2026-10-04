// Add-ons escritos em JavaScript, sem declarações de tipo publicadas.

declare module '@eeacms/volto-pdf-block/components/manage/PDFViewer/BlockView' {
  import type { ComponentType } from 'react';

  /** Dados aceitos pelo bloco de visualização de PDF. */
  export interface PDFBlockData {
    url: string;
    clickToDownload?: boolean;
    hideToolbar?: boolean;
    hideNavbar?: boolean;
    showPagesPreview?: boolean;
    initialPage?: number;
    fitPageWidth?: boolean;
    disableScroll?: boolean;
  }

  const PDFBlockView: ComponentType<{ data: PDFBlockData }>;
  export default PDFBlockView;
}

declare module '@plonegovbr/volto-vlibras/components/Libras' {
  import type { ComponentType } from 'react';

  const Libras: ComponentType;
  export default Libras;
}
