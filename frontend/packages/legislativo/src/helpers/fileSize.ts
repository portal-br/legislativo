const KB = 1000;
const MB = KB * 1000;

/**
 * Formata o tamanho de um arquivo em KB ou MB, arredondado.
 * @param size Tamanho em bytes.
 * @returns Tamanho legível, por exemplo `512 KB` ou `3 MB`.
 */
export function formatFileSize(size: number): string {
  if (size < MB) {
    return `${Math.round(size / KB)} KB`;
  }
  return `${Math.round(size / MB)} MB`;
}
