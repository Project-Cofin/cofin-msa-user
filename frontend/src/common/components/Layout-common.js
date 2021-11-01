import { styled } from '@mui/material/styles';

// const Root = styled(FusePageSimple)({
//   '& .FusePageSimple-header': {},
//   '& .FusePageSimple-toolbar': {},
//   '& .FusePageSimple-content': {},
//   '& .FusePageSimple-sidebarHeader': {},
//   '& .FusePageSimple-sidebarContent': {},
// });

function ExamplePage(props) {
  const { t } = useTranslation('examplePage');

  return (
    <Root
      header={
        <div className="p-24">
          <h4>{t('TITLE')}</h4>
        </div>
      }
      contentToolbar={
        <div className="px-24">
          <h4>Content Toolbar</h4>
          abcd
        </div>
      }
      content={
        <div className="p-24">
          <h4>Content</h4>
          <br />
          <DemoContent />
        </div>
      }
    />
  );
}

export default ExamplePage;
