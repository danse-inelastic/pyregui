

def eval_( expr, d ):
    """evaluate an expression in the current controller. 
    this is only used by renderers like gml.WxRenderer
    """
    if expr == "None": return
    t = "tmp = self.controller.%s" % expr
    try:
        exec t in d
    except Exception, e:
        msg = "Unable to evaluate self.controller.%s. %s: %s" % (
            expr, e.__class__.__name__, e )
        raise RuntimeError , msg
    return d['tmp']
