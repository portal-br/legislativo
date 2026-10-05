import type { JSONSchema } from '@plone/types';
import config from '@plone/volto/registry';
import { defineMessages, type IntlShape } from 'react-intl';
import {
  MAX_COLUMNS,
  type MultiButtonsData,
  type MultiButtonsVariant,
} from './index';

/** Argumentos com que o Volto chama o schema do bloco. */
export interface MultiButtonsSchemaArgs {
  intl: IntlShape;
  data?: MultiButtonsData;
  formData?: MultiButtonsData;
}

const messages = defineMessages({
  block: { id: 'Multiple buttons', defaultMessage: 'Multiple buttons' },
  variant: { id: 'Display', defaultMessage: 'Display' },
  variantDefault: { id: 'Buttons', defaultMessage: 'Buttons' },
  variantCard: { id: 'Cards', defaultMessage: 'Cards' },
  variantImage: { id: 'Images', defaultMessage: 'Images' },
  buttons: { id: 'Button list', defaultMessage: 'Button list' },
  button: { id: 'Button', defaultMessage: 'Button' },
  label: { id: 'Label', defaultMessage: 'Label' },
  labelImage: {
    id: 'Label for screen readers',
    defaultMessage: 'Label for screen readers',
  },
  description: { id: 'Description', defaultMessage: 'Description' },
  href: { id: 'Link', defaultMessage: 'Link' },
  icon: { id: 'Icon', defaultMessage: 'Icon' },
  image: { id: 'Image', defaultMessage: 'Image' },
  altText: { id: 'Alternative text', defaultMessage: 'Alternative text' },
  altTextHelp: {
    id: 'Describe what the button does, for example "Open the transparency portal".',
    defaultMessage:
      'Describe what the button does, for example "Open the transparency portal".',
  },
  openInNewTab: {
    id: 'Open in a new tab',
    defaultMessage: 'Open in a new tab',
  },
  iconNone: { id: 'No icon', defaultMessage: 'No icon' },
  iconArrow: { id: 'Arrow', defaultMessage: 'Arrow' },
  iconPhone: { id: 'Phone', defaultMessage: 'Phone' },
  iconUser: { id: 'Person', defaultMessage: 'Person' },
  iconSummary: { id: 'Summary', defaultMessage: 'Summary' },
  iconCalendar: { id: 'Calendar', defaultMessage: 'Calendar' },
  iconNews: { id: 'News', defaultMessage: 'News' },
  iconCheck: { id: 'Check mark', defaultMessage: 'Check mark' },
  iconEmail: { id: 'E-mail', defaultMessage: 'E-mail' },
  maxColumns: { id: 'Columns', defaultMessage: 'Columns' },
  maxColumnsHelp: {
    id: 'Maximum number of buttons per row. Small screens always show fewer.',
    defaultMessage:
      'Maximum number of buttons per row. Small screens always show fewer.',
  },
  stretch: { id: 'Fill the width', defaultMessage: 'Fill the width' },
  stretchHelp: {
    id: 'Buttons share the full width of the block. Otherwise they all take the width of the widest one.',
    defaultMessage:
      'Buttons share the full width of the block. Otherwise they all take the width of the widest one.',
  },
  theme: { id: 'Background color', defaultMessage: 'Background color' },
});

/** Ícones disponíveis para a variação de botões: nome → mensagem. */
export const ICON_CHOICES = [
  ['arrowRight', messages.iconArrow],
  ['phone', messages.iconPhone],
  ['user', messages.iconUser],
  ['summary', messages.iconSummary],
  ['calendar', messages.iconCalendar],
  ['image', messages.image],
  ['news', messages.iconNews],
  ['link', messages.href],
  ['check', messages.iconCheck],
  ['email', messages.iconEmail],
] as const;

const FIELDS: Record<MultiButtonsVariant, string[]> = {
  default: ['title', 'href', 'icon', 'openInNewTab'],
  card: ['title', 'description', 'href', 'openInNewTab'],
  image: ['title', 'image', 'altText', 'href', 'openInNewTab'],
};

const linkField = (title: string) => ({
  title,
  widget: 'object_browser',
  mode: 'link',
  allowExternals: true,
  selectedItemAttrs: ['Title', '@type', 'image_field', 'image_scales'],
});

/**
 * Schema de cada botão: os campos dependem da variação do bloco.
 * @param intl Objeto de internacionalização.
 * @param variant Variação do bloco.
 * @returns Schema de um item da lista de botões.
 */
export function buttonSchema(
  intl: IntlShape,
  variant: MultiButtonsVariant,
): JSONSchema {
  const t = intl.formatMessage;
  return {
    title: t(messages.button),
    fieldsets: [{ id: 'default', title: 'Default', fields: FIELDS[variant] }],
    properties: {
      title: {
        title: t(variant === 'image' ? messages.labelImage : messages.label),
      },
      description: { title: t(messages.description), widget: 'textarea' },
      href: linkField(t(messages.href)),
      icon: {
        title: t(messages.icon),
        choices: ICON_CHOICES.map(([name, message]) => [name, t(message)]),
        noValueOption: true,
      },
      image: linkField(t(messages.image)),
      altText: {
        title: t(messages.altText),
        description: t(messages.altTextHelp),
      },
      openInNewTab: { title: t(messages.openInNewTab), type: 'boolean' },
    },
    required: variant === 'image' ? ['image', 'altText'] : [],
  };
}

/**
 * Schema do bloco de múltiplos botões.
 * @param args Argumentos do Volto: `intl` e os dados do bloco.
 * @returns Schema do bloco.
 */
export function multiButtonsSchema({
  intl,
  data,
  formData,
}: MultiButtonsSchemaArgs): JSONSchema {
  const variant = (data ?? formData)?.variant ?? 'default';
  const themes = config.blocks.themes ?? [];
  const t = intl.formatMessage;
  return {
    title: t(messages.block),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['variant', 'buttons', 'maxColumns', 'stretch', 'theme'],
      },
    ],
    properties: {
      variant: {
        title: t(messages.variant),
        choices: [
          ['default', t(messages.variantDefault)],
          ['card', t(messages.variantCard)],
          ['image', t(messages.variantImage)],
        ],
        default: 'default',
        noValueOption: false,
      },
      buttons: {
        title: t(messages.buttons),
        widget: 'object_list',
        schema: buttonSchema(intl, variant),
      },
      maxColumns: {
        title: t(messages.maxColumns),
        description: t(messages.maxColumnsHelp),
        type: 'integer',
        minimum: 1,
        maximum: MAX_COLUMNS,
        default: 3,
      },
      stretch: {
        title: t(messages.stretch),
        description: t(messages.stretchHelp),
        type: 'boolean',
        default: false,
      },
      theme: {
        title: t(messages.theme),
        widget: 'color_picker',
        themes,
        default: themes[0]?.name,
      },
    },
    required: [],
  };
}
