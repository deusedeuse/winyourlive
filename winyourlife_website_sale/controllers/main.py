# -*- coding: utf-8 -*-
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleInherit(WebsiteSale):
    def redirect_if_not_logged_in(self, url_after_redirect="/shop/cart"):
        """
        Check if user is logged in, else redirect it to login page
        :return: need_redirect, whether the user should be redirect or not
        :return: redirection, the redirection to return by the function
        """
        # Check if user is logged in
        if request.env.user.id == request.env.ref('base.public_user').id:
            # Enforce the user to be logged in
            return True, request.redirect('/web/login?redirect=%s' % url_after_redirect)
        else:
            return False, None

    @http.route()
    def address(self, **kw):
        # Check if user is logged in
        need_redirect, redirection = self.redirect_if_not_logged_in("/shop/cart")
        if need_redirect:
            return redirection
        else:
            return super().address(**kw)

    @http.route()
    def checkout(self, **post):
        # Check if user is logged in
        need_redirect, redirection = self.redirect_if_not_logged_in("/shop/cart")
        if need_redirect:
            return redirection
        else:
            return super().checkout(**post)

    @http.route()
    def shop_payment(self, **post):
        # Check if user is logged in
        need_redirect, redirection = self.redirect_if_not_logged_in("/shop/cart")
        if need_redirect:
            return redirection
        else:
            return super().shop_payment(**post)

    def _get_mandatory_fields_billing(self, country_id=False):
        """Overwrite the method in order to reduce the fields required to make a purchase from the website"""
        req = ["name", "email"]
        return req

    def _get_mandatory_fields_shipping(self, country_id=False):
        """Overwrite the method in order to reduce the fields required to make a purchase from the website"""
        req = ["name"]
        return req