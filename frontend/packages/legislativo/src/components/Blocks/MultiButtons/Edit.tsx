import { useIntl } from 'react-intl';
import BlockDataForm from '@plone/volto/components/manage/Form/BlockDataForm';
import SidebarPortal from '@plone/volto/components/manage/Sidebar/SidebarPortal';
import { multiButtonsSchema } from './schema';
import View from './View';
import type { MultiButtonsData } from './index';

interface EditProps {
  data: MultiButtonsData;
  block: string;
  selected: boolean;
  onChangeBlock: (id: string, data: MultiButtonsData) => void;
  className?: string;
}

/**
 * Edição do bloco de múltiplos botões: a visão e o formulário na barra lateral.
 * @param props Propriedades de edição de bloco do Volto.
 * @returns Markup do bloco em modo de edição.
 */
const Edit = (props: EditProps) => {
  const { data, block, selected, onChangeBlock, className } = props;
  const intl = useIntl();
  const schema = multiButtonsSchema({ intl, data });

  return (
    <>
      <View data={data} className={className} isEditMode />
      <SidebarPortal selected={selected}>
        <BlockDataForm
          schema={schema}
          title={schema.title}
          onChangeField={(id: string, value: unknown) =>
            onChangeBlock(block, { ...data, [id]: value })
          }
          onChangeBlock={onChangeBlock}
          formData={data}
          block={block}
        />
      </SidebarPortal>
    </>
  );
};

export default Edit;
