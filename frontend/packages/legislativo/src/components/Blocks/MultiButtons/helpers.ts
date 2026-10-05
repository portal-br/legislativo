import type { CSSProperties } from 'react';
import { flattenToAppURL, isInternalURL } from '@plone/volto/helpers/Url/Url';
import type { LinkTarget, MultiButtonsData, MultiButtonsItem } from './index';

/** Tema de bloco registrado em `config.blocks.themes`. */
export interface BlockTheme {
  name: string;
  style: Record<string, string>;
}

/**
 * Primeiro alvo de um campo `object_browser` (lista) ou de um texto.
 * @param value Valor salvo no campo.
 * @returns O alvo, ou `undefined` quando o campo está vazio.
 */
export function firstTarget(
  value: LinkTarget[] | string | undefined,
): LinkTarget | undefined {
  if (Array.isArray(value)) return value[0];
  const url = value?.trim();
  return url ? { '@id': url } : undefined;
}

/**
 * URL de um campo `object_browser` ou de um texto.
 * @param value Valor salvo no campo.
 * @returns A URL, ou `undefined` quando o campo está vazio.
 */
export function targetURL(
  value: LinkTarget[] | string | undefined,
): string | undefined {
  return firstTarget(value)?.['@id'] || undefined;
}

/**
 * Endereço da imagem de um botão: conteúdo interno usa a escala padrão.
 * @param url URL do conteúdo ou da imagem.
 * @returns Endereço para o atributo `src`.
 */
export function imageSrc(url: string): string {
  if (!isInternalURL(url)) return url;
  const path = flattenToAppURL(url).replace(/\/+$/, '');
  return path.includes('@@images') ? path : `${path}/@@images/image`;
}

/**
 * Rótulo acessível de um botão: texto alternativo, título ou descrição.
 * Endereços não servem de rótulo.
 * @param item Botão.
 * @returns O rótulo, ou `undefined` quando não há texto adequado.
 */
export function accessibleLabel(item: MultiButtonsItem): string | undefined {
  const label = (item.altText || item.title || item.description || '').trim();
  const isURL = /^https?:\/\//i.test(label) || label.startsWith('/');
  return label && !isURL ? label : undefined;
}

/**
 * Número de colunas: o máximo escolhido, limitado ao número de botões.
 * @param maxColumns Máximo escolhido no editor.
 * @param count Número de botões.
 * @returns Colunas, no mínimo 1.
 */
export function columns(maxColumns: number | undefined, count: number): number {
  const wanted =
    maxColumns && Number.isFinite(maxColumns) && maxColumns > 0
      ? Math.floor(maxColumns)
      : count;
  return Math.max(1, Math.min(wanted, count));
}

/**
 * Variáveis CSS do tema escolhido para o bloco.
 * @param data Dados do bloco.
 * @param themes Temas disponíveis.
 * @returns Estilo com as variáveis do tema, ou vazio.
 */
export function themeStyle(
  data: MultiButtonsData,
  themes: BlockTheme[],
): CSSProperties {
  return themes.find((theme) => theme.name === data.theme)?.style ?? {};
}
