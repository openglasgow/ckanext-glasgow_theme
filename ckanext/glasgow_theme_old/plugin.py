import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class GlasgowThemePlugin(plugins.SingletonPlugin):
    '''Glasgow's Theme for data.glasgow.gov.uk

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    
    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'theme/templates')
        
        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'theme/public')
        
        toolkit.add_resource('theme/fanstatic', 'glasgow')
