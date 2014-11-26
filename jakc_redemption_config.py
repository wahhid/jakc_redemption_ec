from openerp.osv import fields, osv
import logging

_logger = logging.getLogger(__name__)

class rdm_config(osv.osv):
    _name = 'rdm.config'
    _description = 'Redemption Config'
    
    def get_redemption_config(self, cr, uid, context=None):
        ids = self.search(cr, uid, [('state','=', True),], context=context)
        if ids:
            return self.browse(cr, uid, uid, context=context)
        else:
            return None
            
    _columns = {
        'enable_email' : fields.boolean('Enable Email'),
        'pop3_download': fields.boolean('POP3 Download'),
        'pop3_server': fields.char('POP3 Server', size=50),
        'pop3_user': fields.char('POP3 User', size=50),
        'pop3_password': fields.char('POP3 Password', size=50),
        'state': fields.boolean('Status'),
    }
    
    _defaults = {
        'enable_email': lambda *a: False,
        'pop3_download': lambda *a: False,
        'state': lambda *a: True,
    }
    
rdm_config()

class rdm_config_settings(osv.osv_memory):
    _name = 'rdm.config.settings'
    _inherit = 'res.config.settings'
    _columns = {
        'enable_email' : fields.boolean('Enable Email'),
        'pop3_download': fields.boolean('POP3 Download'),
        'pop3_server': fields.char('POP3 Server', size=50),
        'pop3_user': fields.char('POP3 User', size=50),
        'pop3_password': fields.char('POP3 Password', size=50),
    }

    def _get_config(self, cr, uid, context=None):
        ids = self.pool.get('rdm.config').search(cr, uid, [('state','=', True),], context=context)
        if ids:
            config  = self.pool.get('rdm.config').browse(cr, uid, ids[0], context=context)
        else:
            config = None
        return config
    
    def get_default_enable_email(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            enable_email = config.enable_email 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            enable_email = False
        return {'enable_email': enable_email}


    def set_default_enable_email(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        enable_email = setting.enable_email
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'enable_email': enable_email})

    def get_default_pop3_download(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_download = config.pop3_download 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_download = False
        return {'pop3_download': pop3_download}


    def set_default_pop3_download(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_download = setting.pop3_download
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_download': pop3_download})    
        
    def get_default_pop3_server(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_server = config.pop3_server 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_server = False
        return {'pop3_server': pop3_server}


    def set_default_pop3_server(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_server = setting.pop3_server
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_server': pop3_server})
        
    def get_default_pop3_user(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_user = config.pop3_user
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_user = False
        return {'pop3_user': pop3_user}


    def set_default_pop3_user(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_user = setting.pop3_user
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_user': pop3_user})
        
    def get_default_pop3_password(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_password = config.pop3_password
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_password = False
        return {'pop3_password': pop3_password}


    def set_default_pop3_password(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_password = setting.pop3_password
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_password': pop3_password})
        
    
    
        
     