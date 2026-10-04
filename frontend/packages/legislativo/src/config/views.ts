import type { ComponentType } from 'react';
import type { ConfigType } from '@plone/registry';
// Views
import FileView from '../components/Views/FileView';

export default function install(config: ConfigType) {
  /// Content Types
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    // The registry types views without props; Volto's View passes
    // `content` and `location` to them at runtime.
    File: FileView as ComponentType,
  };

  return config;
}
