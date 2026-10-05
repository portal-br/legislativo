import type { Content } from '@plone/types';

/** Arquivo armazenado em um campo de arquivo do Plone. */
export interface NamedFile {
  'content-type': string;
  download: string;
  filename: string;
  size: number;
}

/** Conteúdo do tipo Arquivo. */
export interface FileContent extends Content {
  file?: NamedFile | null;
}

/** Props comuns às views de tipo de conteúdo do Portal Modelo. */
export interface ContentTypeViewProps<T extends Content = Content> {
  content: T;
  location?: { pathname: string };
}
