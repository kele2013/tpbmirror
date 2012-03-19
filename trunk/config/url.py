#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'view.index',
    '/tpbtop',              pre_fix + 'view.topview',
    '/tpbtop/.*',           pre_fix + 'view.typeview',
    '/recent',              pre_fix + 'view.recentview',
    '/search',              pre_fix + 'view.searchview',
    '/help',                pre_fix + 'view.simpletpb_help',
    '/resourceinfoid/.*',   pre_fix + 'view.resource_info',
    '/fetch',               pre_fix + 'daemon.daemon_fetch',
    '/testdb',              pre_fix + 'test.testdb',
    '/testfetchtop',        pre_fix + 'test.testfetchtop',
    '/testfetchall',        pre_fix + 'test.testfetchall',
)
