import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { NotebookActions } from '@jupyterlab/notebook';

/**
 * Initialization data for the jupyterlab-cell-flash extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-cell-flash',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    NotebookActions.executed.connect((_, args) => {
      const { cell } = args;
      const element = cell.editor.host;
      element.classList.remove('flash-effect');
      element.offsetWidth;
      const onAnimationEnd = () => {
        element.removeEventListener('animationcancel', onAnimationEnd);
        element.removeEventListener('animationend', onAnimationEnd);
        element.classList.remove('flash-effect');
      };
      requestAnimationFrame(() => {
        element.addEventListener('animationend', onAnimationEnd);
        element.addEventListener('animationcancel', onAnimationEnd);
        element.classList.add('flash-effect');
      });
    });
  }
};

export default extension;
