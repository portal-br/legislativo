import type { BlockConfigBase } from '@plone/types';
import gridSVG from '@plone/volto/icons/grid.svg';
import Edit from './Edit';
import View from './View';
import { multiButtonsSchema } from './schema';

export const BLOCK_ID = 'multiButtons';

/** Maior número de colunas que o editor pode escolher. */
export const MAX_COLUMNS = 6;

export type MultiButtonsVariant = 'default' | 'card' | 'image';

/** Valor de um campo `object_browser` em modo link. */
export interface LinkTarget {
  '@id'?: string;
  title?: string;
  image_field?: string;
  image_scales?: Record<string, unknown>;
}

export interface MultiButtonsItem {
  '@id'?: string;
  title?: string;
  description?: string;
  href?: LinkTarget[] | string;
  icon?: string;
  image?: LinkTarget[] | string;
  altText?: string;
  openInNewTab?: boolean;
}

export interface MultiButtonsData {
  '@type'?: string;
  variant?: MultiButtonsVariant;
  buttons?: MultiButtonsItem[];
  maxColumns?: number;
  stretch?: boolean;
  theme?: string;
}

const MultiButtonsBlockInfo: BlockConfigBase = {
  id: BLOCK_ID,
  // O BlockChooser do Volto traduz o título como id de mensagem.
  title: 'Multiple buttons',
  icon: gridSVG,
  group: 'common',
  view: View,
  edit: Edit,
  // O Volto chama o schema com `intl` e os dados do bloco; os tipos de
  // `@plone/types` usam outra declaração de IntlShape que a do react-intl.
  blockSchema: multiButtonsSchema as unknown as BlockConfigBase['blockSchema'],
  restricted: false,
  mostUsed: false,
  sidebarTab: 1,
};

export default MultiButtonsBlockInfo;
