import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import Wrapper from '@plone/volto/storybook';
import Edit from './Edit';

vi.mock('@plone/volto/components/manage/Sidebar/SidebarPortal', () => ({
  default: ({
    children,
    selected,
  }: {
    children: React.ReactNode;
    selected: boolean;
  }) => (selected ? <div data-testid="sidebar">{children}</div> : null),
}));

vi.mock('@plone/volto/components/manage/Form/BlockDataForm', () => ({
  default: ({
    title,
    onChangeField,
  }: {
    title: string;
    onChangeField: (id: string, value: unknown) => void;
  }) => (
    <button type="button" onClick={() => onChangeField('stretch', true)}>
      {title}
    </button>
  ),
}));

describe('MultiButtons Edit', () => {
  it('mostra o bloco e o formulário na barra lateral', () => {
    const onChangeBlock = vi.fn();
    const data = {
      variant: 'default' as const,
      buttons: [{ title: 'Ouvidoria', href: '/o' }],
    };
    render(
      <Wrapper anonymous>
        <Edit data={data} block="b1" selected onChangeBlock={onChangeBlock} />
      </Wrapper>,
    );
    expect(screen.getByText('Ouvidoria')).toBeTruthy();
    expect(screen.queryByRole('link')).toBeNull();
    fireEvent.click(screen.getByRole('button', { name: 'Multiple buttons' }));
    expect(onChangeBlock).toHaveBeenCalledWith('b1', {
      ...data,
      stretch: true,
    });
  });

  it('esconde o formulário quando o bloco não está selecionado', () => {
    render(
      <Wrapper anonymous>
        <Edit data={{}} block="b1" selected={false} onChangeBlock={vi.fn()} />
      </Wrapper>,
    );
    expect(screen.queryByTestId('sidebar')).toBeNull();
  });
});
