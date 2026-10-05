import type { CSSProperties, ReactNode } from 'react';
import cx from 'classnames';
import { defineMessages, useIntl } from 'react-intl';
import config from '@plone/volto/registry';
import ConditionalLink from '@plone/volto/components/manage/ConditionalLink/ConditionalLink';
import Icon from '@plone/volto/components/theme/Icon/Icon';
import Image from '@plone/volto/components/theme/Image/Image';
import arrowRightSVG from '@plone/volto/icons/right-key.svg';
import calendarSVG from '@plone/volto/icons/calendar.svg';
import checkSVG from '@plone/volto/icons/check.svg';
import emailSVG from '@plone/volto/icons/email.svg';
import imageSVG from '@plone/volto/icons/image.svg';
import linkSVG from '@plone/volto/icons/link.svg';
import newsSVG from '@plone/volto/icons/news.svg';
import phoneSVG from '@plone/volto/icons/mobile.svg';
import summarySVG from '@plone/volto/icons/summary.svg';
import userSVG from '@plone/volto/icons/user.svg';
import {
  accessibleLabel,
  columns,
  firstTarget,
  imageSrc,
  targetURL,
  themeStyle,
  type BlockTheme,
} from './helpers';
import type { MultiButtonsData, MultiButtonsItem } from './index';

const messages = defineMessages({
  empty: {
    id: 'Add buttons in the sidebar.',
    defaultMessage: 'Add buttons in the sidebar.',
  },
  selectImage: { id: 'Select an image', defaultMessage: 'Select an image' },
});

export const ICONS: Record<string, unknown> = {
  arrowRight: arrowRightSVG,
  calendar: calendarSVG,
  check: checkSVG,
  email: emailSVG,
  image: imageSVG,
  link: linkSVG,
  news: newsSVG,
  phone: phoneSVG,
  summary: summarySVG,
  user: userSVG,
};

interface ButtonProps {
  item: MultiButtonsItem;
  variant: MultiButtonsData['variant'];
  isEditMode: boolean;
}

/**
 * Conteúdo de um botão, conforme a variação do bloco.
 * @param props Botão, variação e modo de edição.
 * @returns Markup do conteúdo do botão.
 */
const ButtonContent = ({ item, variant, isEditMode }: ButtonProps) => {
  const intl = useIntl();
  if (variant === 'card') {
    return (
      <>
        {item.title && (
          <h2 className="multi-buttons-card-title">{item.title}</h2>
        )}
        {item.description && (
          <p className="multi-buttons-card-description">{item.description}</p>
        )}
      </>
    );
  }
  if (variant === 'image') {
    const target = firstTarget(item.image);
    const alt = accessibleLabel(item) ?? '';
    let image: ReactNode = null;
    if (target?.image_scales) {
      image = <Image item={target} alt={alt} loading="lazy" />;
    } else if (target?.['@id']) {
      image = <Image src={imageSrc(target['@id'])} alt={alt} loading="lazy" />;
    } else if (isEditMode) {
      image = (
        <span className="multi-buttons-image-placeholder">
          {intl.formatMessage(messages.selectImage)}
        </span>
      );
    }
    return <span className="multi-buttons-image-frame">{image}</span>;
  }
  const icon = item.icon ? ICONS[item.icon] : undefined;
  return (
    <>
      {icon ? <Icon name={icon} size="20px" /> : null}
      <span className="multi-buttons-label">{item.title}</span>
    </>
  );
};

interface ViewProps {
  data: MultiButtonsData;
  className?: string;
  style?: CSSProperties;
  isEditMode?: boolean;
}

/**
 * Bloco de múltiplos botões: links lado a lado, como botões, cards ou imagens.
 * @param props Dados do bloco, classe e estilo do wrapper do Volto.
 * @returns Markup do bloco.
 */
const View = ({ data, className, style, isEditMode = false }: ViewProps) => {
  const intl = useIntl();
  const items = data.buttons ?? [];
  const variant = data.variant ?? 'default';
  if (!items.length && !isEditMode) return null;
  const themes = (config.blocks.themes ?? []) as BlockTheme[];
  const listStyle = {
    '--multi-buttons-cols': columns(data.maxColumns, items.length),
  } as CSSProperties;

  return (
    <div
      className={cx(
        'block',
        'multi-buttons-block',
        `is-variant-${variant}`,
        className,
      )}
      style={{ ...style, ...themeStyle(data, themes) }}
    >
      {items.length ? (
        <ul
          className={cx('multi-buttons-block__list', {
            'is-stretch': data.stretch,
          })}
          style={listStyle}
        >
          {items.map((item, index) => {
            const href = targetURL(item.href);
            const label = accessibleLabel(item);
            return (
              <li
                className={cx('multi-buttons-block__item', {
                  'is-disabled': !href,
                })}
                key={item['@id'] ?? index}
              >
                <ConditionalLink
                  condition={!isEditMode && !!href}
                  href={href}
                  className="multi-buttons-block__button"
                  openLinkInNewTab={item.openInNewTab ?? false}
                  aria-label={variant === 'image' ? label : undefined}
                >
                  <ButtonContent
                    item={item}
                    variant={variant}
                    isEditMode={isEditMode}
                  />
                </ConditionalLink>
              </li>
            );
          })}
        </ul>
      ) : (
        <p className="multi-buttons-block__empty">
          {intl.formatMessage(messages.empty)}
        </p>
      )}
    </div>
  );
};

export default View;
