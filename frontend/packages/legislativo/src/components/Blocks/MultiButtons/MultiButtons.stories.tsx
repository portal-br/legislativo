import type { ComponentType } from 'react';
import Wrapper from '@plone/volto/storybook';
import View from './View';
import type { MultiButtonsData } from './index';

const withWrapper = (Story: ComponentType) => (
  <Wrapper anonymous>
    <div style={{ width: '1000px', padding: '1rem', backgroundColor: 'white' }}>
      <Story />
    </div>
  </Wrapper>
);

const meta = {
  title: 'Public/Blocks/MultiButtons',
  component: View,
  decorators: [withWrapper],
};

export default meta;

const image = (seed: string) => [
  { '@id': `https://picsum.photos/seed/${seed}/400/300` },
];

export const Botoes = {
  args: {
    data: {
      variant: 'default',
      maxColumns: 4,
      buttons: [
        { title: 'Ouvidoria', href: '/ouvidoria', icon: 'phone' },
        { title: 'Agenda', href: '/agenda', icon: 'calendar' },
        { title: 'Notícias', href: '/noticias', icon: 'news' },
        { title: 'Fale conosco', href: '/contato', icon: 'email' },
      ],
    } satisfies MultiButtonsData,
  },
};

export const BotoesLarguraTotal = {
  args: {
    data: { ...Botoes.args.data, stretch: true, maxColumns: 2 },
  },
};

export const Cards = {
  args: {
    data: {
      variant: 'card',
      maxColumns: 3,
      buttons: [
        {
          title: 'Licitações',
          description: 'Editais, atas e contratos da casa legislativa.',
          href: '/transparencia/licitacoes',
        },
        {
          title: 'Diárias',
          description: 'Diárias pagas a vereadores e servidores.',
          href: '/transparencia/diarias',
        },
        {
          title: 'Folha de pagamento',
          description: 'Remuneração de agentes públicos.',
          href: '/transparencia/folha',
        },
      ],
    } satisfies MultiButtonsData,
  },
};

export const Imagens = {
  args: {
    data: {
      variant: 'image',
      maxColumns: 3,
      buttons: [
        {
          altText: 'Portal da transparência',
          image: image('portal-modelo-1'),
          href: '/transparencia',
        },
        {
          altText: 'Sessões ao vivo',
          image: image('portal-modelo-2'),
          href: '/sessoes',
        },
        {
          altText: 'Leis municipais',
          image: image('portal-modelo-3'),
          href: '/leis',
        },
      ],
    } satisfies MultiButtonsData,
  },
};

export const Vazio = {
  args: { data: {}, isEditMode: true },
};
