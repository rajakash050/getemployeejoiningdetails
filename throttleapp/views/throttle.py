from awaazapp.models.getmembers import *
from awaazapp.common.db import getquery
from django.http import Http404,HttpResponse, HttpResponseBadRequest,HttpRequest
import json

import projectname.settings as settings
domain_url = settings.SITE_URL

def getMemberDetails(limit=None):
    if limit == None:
        limit = 100
    get_article = "select * from member LIMIT {}".format(limit)
    response = getquery(get_article)
    return response

def getMmemberActivity(memberid):
    get_activity = "SELECT * from activity_periods WHERE memberid={}".format(memberid)
    response = getquery(get_activity)
    # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    activity_res = []
    for i in response:
        # i['start_date'] = str(i['start_date'].strftime('%m/%d/%Y'))
        # i['end_date'] = str(i['end_date'].strftime('%m/%d/%Y'))
        temp_res = {'start_date': str(i['start_date'].strftime('%m/%d/%Y')),
                        'end_date': str(i['end_date'].strftime('%m/%d/%Y'))}
        activity_res.append(temp_res)
        # print(i['start_date'])
    # print("iiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    return activity_res

def iterate(lst, start, end , final_resp):
    if start < 0 or end >= len(lst) or start > end:
        return final_resp
    # print(lst[start])

    activity_resp = getMmemberActivity(lst[start]['memberid'])
    temp_resp = {}
    temp_resp = {"id":lst[start]['memberid'],"member_name":lst[start]['member_name'],"member_desc":lst[start]['member_desc']}
    temp_resp['activity_periods'] = activity_resp

    final_resp['members'].append(temp_resp)

    iterate(lst, start + 1, end, final_resp)

    return final_resp



def get_all_member(requests):
    get_member_details = getMemberDetails()

    # print(get_member_details)

    final_resp = {"ok":True,'members':[]}
    final_resp = iterate(get_member_details, 0, (len(get_member_details) - 1), final_resp)
    print(json.dumps(final_resp))
    bb = json.dumps(final_resp)
    return HttpResponse(bb)

