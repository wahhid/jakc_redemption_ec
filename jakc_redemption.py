from openerp.osv import fields, osv

class rdm_customer_type(osv.osv):
    _name = "rdm.customer.type"
    _description = "Customer Type"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_type()

class rdm_customer_ethnic(osv.osv):
    _name = "rdm.customer.ethnic"
    _description = "Customer Ethic"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_ethnic()

class rdm_customer_religion(osv.osv):
    _name = "rdm.customer.religion"
    _description = "Customer Religion"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_religion()

class rdm_customer_gender(osv.osv):
    _name = "rdm.customer.gender"
    _description = "Customer Gender"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_gender()

class rdm_customer_marital(osv.osv):
    _name = "rdm.customer.marital"
    _description = "Customer Marital"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_marital()

class rdm_customer_zone(osv.osv):
    _name = "rdm.customer.zone"
    _description = "Customer Residential Zone"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_zone()

class rdm_customer_education(osv.osv):
    _name = "rdm.customer.education"
    _description = "Customer Education"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_education()

class rdm_customer_interest(osv.osv):
    _name = "rdm.customer.interest"
    _description = "Customer Interest"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_customer_interest()

class rdm_customer_occupation(osv.osv):
    _name = "rdm.customer.occupation"
    _description = "Customer Occupation"
    _columns = {
        'name': fields.char('Name', size=100, required=True),
    }

class rdm_card_type(osv.osv):
    _name = "rdm.card.type"
    _description = "Card Type"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_card_type()


class rdm_tenant_category(osv.osv):
    _name = "rdm.tenant.category"
    _description = "Tenant Category"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_tenant_category()

class rdm_tenant_grade(osv.osv):
    _name = "rdm.tenant.grade"
    _description = "Tenant Grade"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_tenant_grade()

class rdm_bank(osv.osv):
    _name = "rdm.bank"
    _description = "Bank"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),        
        'bank_card_ids': fields.one2many('rdm.bank.card','bank_id','Bank Card'),     
    }    
rdm_bank()

class rdm_bank_card(osv.osv):
    _name = "rdm.bank.card"
    _description = "Bank Card"
    _columns = {        
        'bank_id': fields.many2one('rdm.bank','Bank ID'),
        'card_type': fields.selection([('debit','Debit'),('silver','Silver'),('gold','Gold'),('titanium','Titanium'),('platinum','Platinum')],'Card Type', required=True),           
        'name': fields.char('Name', size=100, required=True),                    
    }    
    _defaults = {
        'bank_id': lambda self, cr, uid, context: context.get('bank_id', False),
    }    
rdm_bank_card()

class rdm_tenant_title(osv.osv):
    _name = "rdm.tenant.title"
    _description = "Tenant Title"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_tenant_title()    

class rdm_province(osv.osv):
    _name = "rdm.province"
    _description = "Province"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_province()    

class rdm_city(osv.osv):
    _name = "rdm.city"
    _description = "City"
    _columns = {        
        'name': fields.char('Name', size=100, required=True),            
    }    
rdm_city()

class rdm_age_segment(osv.osv):
    _name = 'rdm.age.segment'
    _description = 'Redemption Age Segment'
    _columns = {
        'name': fields.char('Name', size=200, readonly=True),
        'start_age': fields.integer('Start Age', required=True),
        'end_age': fields.integer('End Age', required=True),        
    }    
    
    def create(self, cr, uid, values, context=None):
        values.update({'name':str(values['start_age']) + " to " + str(values['end_age']) + " Years"})        
        return super(rdm_age_segment,self).create(cr,uid,values,context=context)
    
    def write(self, cr, uid, ids, values, context=None):
        values.update({'name':str(values['start_age']) + " to " + str(values['end_age']) + " Years"})        
        return super(rdm_age_segment,self).write(cr, uid, ids, values,context=context)
    
rdm_age_segment()
