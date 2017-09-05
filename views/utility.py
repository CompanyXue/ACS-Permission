# -*- coding:UTF-8 -*-


def true_return(data, msg):
    return {
        'status': True,
        'data': data,
        'msg': msg
    }


def false_return(data, msg):
    return {
        'status': False,
        'data': data,
        'msg': msg
    }
