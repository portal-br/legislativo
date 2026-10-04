import { describe, expect, it } from 'vitest';
import { formatFileSize } from './fileSize';

describe('formatFileSize', () => {
  it.each([
    [0, '0 KB'],
    [1499, '1 KB'],
    [512000, '512 KB'],
    [999999, '1000 KB'],
    [1000000, '1 MB'],
    [3400000, '3 MB'],
  ])('formata %i bytes como %s', (size, expected) => {
    expect(formatFileSize(size)).toBe(expected);
  });
});
