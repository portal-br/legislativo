import { render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it } from 'vitest';
import config from '@plone/volto/registry';
import Wrapper from '@plone/volto/storybook';
import View from './View';
import type { MultiButtonsData } from './index';

const originalThemes = config.blocks.themes;

afterEach(() => {
  config.blocks.themes = originalThemes;
});

const api = () => config.settings.apiPath;

const renderView = (data: MultiButtonsData, isEditMode = false) =>
  render(
    <Wrapper anonymous>
      <View data={data} isEditMode={isEditMode} />
    </Wrapper>,
  );

const block = (container: HTMLElement) =>
  container.querySelector('.multi-buttons-block') as HTMLElement;

describe('MultiButtons View', () => {
  it('não mostra nada sem botões', () => {
    const { container } = renderView({});
    expect(block(container)).toBeNull();
  });

  it('pede botões em modo de edição', () => {
    renderView({}, true);
    expect(screen.getByText('Add buttons in the sidebar.')).toBeTruthy();
  });

  it('mostra botões com link e ícone', () => {
    const { container } = renderView({
      buttons: [
        {
          title: 'Ouvidoria',
          href: [{ '@id': `${api()}/ouvidoria` }],
          icon: 'phone',
        },
        { title: 'Sem ícone', href: 'https://example.org', openInNewTab: true },
      ],
    });
    const links = screen.getAllByRole('link');
    expect(links.map((a) => a.getAttribute('href'))).toEqual([
      '/ouvidoria',
      'https://example.org',
    ]);
    expect(links[1].getAttribute('target')).toBe('_blank');
    expect(container.querySelectorAll('svg')).toHaveLength(1);
    expect(block(container).className).toContain('is-variant-default');
  });

  it('ignora ícone desconhecido', () => {
    const { container } = renderView({
      buttons: [{ title: 'Botão', href: '/a', icon: 'desconhecido' }],
    });
    expect(container.querySelectorAll('svg')).toHaveLength(0);
  });

  it('desabilita botão sem link', () => {
    const { container } = renderView({ buttons: [{ title: 'Em breve' }] });
    expect(screen.queryByRole('link')).toBeNull();
    expect(container.querySelector('.is-disabled')).not.toBeNull();
  });

  it('não cria links em modo de edição', () => {
    renderView({ buttons: [{ title: 'Ouvidoria', href: '/ouvidoria' }] }, true);
    expect(screen.queryByRole('link')).toBeNull();
    expect(screen.getByText('Ouvidoria')).toBeTruthy();
  });

  it('define colunas e largura total', () => {
    const { container } = renderView({
      maxColumns: 2,
      stretch: true,
      buttons: [{ title: 'A' }, { title: 'B' }, { title: 'C' }],
    });
    const list = container.querySelector('ul') as HTMLElement;
    expect(list.style.getPropertyValue('--multi-buttons-cols')).toBe('2');
    expect(list.className).toContain('is-stretch');
  });

  it('mostra cards com título e descrição', () => {
    renderView({
      variant: 'card',
      buttons: [
        { title: 'Licitações', description: 'Editais abertos', href: '/a' },
        { href: '/b' },
      ],
    });
    expect(screen.getByRole('heading', { name: 'Licitações' })).toBeTruthy();
    expect(screen.getByText('Editais abertos')).toBeTruthy();
    expect(screen.getAllByRole('heading')).toHaveLength(1);
  });

  it('mostra imagens com texto alternativo', () => {
    renderView({
      variant: 'image',
      buttons: [
        {
          altText: 'Portal da transparência',
          image: [{ '@id': `${api()}/imagens/transparencia` }],
          href: '/transparencia',
        },
        {
          title: 'Com escalas',
          image: [
            {
              '@id': `${api()}/imagens/foto`,
              image_field: 'image',
              image_scales: {
                image: [
                  {
                    download: '@@images/image.png',
                    width: 400,
                    height: 300,
                    scales: {},
                  },
                ],
              },
            },
          ],
        },
      ],
    });
    const images = screen.getAllByRole('img');
    expect(images[0].getAttribute('src')).toBe(
      '/imagens/transparencia/@@images/image',
    );
    expect(images[0].getAttribute('alt')).toBe('Portal da transparência');
    expect(images[1].getAttribute('src')).toBe(
      '/imagens/foto/@@images/image.png',
    );
    expect(screen.getByRole('link').getAttribute('aria-label')).toBe(
      'Portal da transparência',
    );
  });

  it('pede imagem em modo de edição e omite fora dele', () => {
    const data: MultiButtonsData = {
      variant: 'image',
      buttons: [{ title: 'Sem imagem' }],
    };
    renderView(data, true);
    expect(screen.getByText('Select an image')).toBeTruthy();
  });

  it('não mostra placeholder de imagem para visitantes', () => {
    const { container } = renderView({
      variant: 'image',
      buttons: [{ href: '/a' }],
    });
    expect(
      container.querySelector('.multi-buttons-image-frame')?.innerHTML,
    ).toBe('');
    expect(screen.getByRole('link').getAttribute('aria-label')).toBeNull();
  });

  it('aplica as variáveis do tema escolhido', () => {
    config.blocks.themes = [
      { name: 'brand', label: 'Brand', style: { '--theme-color': 'blue' } },
    ];
    const { container } = renderView({
      theme: 'brand',
      buttons: [{ title: 'A' }],
    });
    expect(block(container).style.getPropertyValue('--theme-color')).toBe(
      'blue',
    );
  });

  it('funciona sem temas de bloco', () => {
    config.blocks.themes = undefined as unknown as typeof originalThemes;
    const { container } = renderView({
      theme: 'brand',
      buttons: [{ title: 'A' }],
    });
    expect(block(container)).not.toBeNull();
  });
});
