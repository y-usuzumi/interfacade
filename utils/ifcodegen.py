__author__ = 'kj'

class IFCodeGen:
    @classmethod
    def _class_gen(cls, stub):
        clstmpl = \
        '''class {clsname}{clsattrs}:
{indent}pass'''
        attrtmpl = \
        '''({attrs})'''
        bases = getattr(stub, 'inherited_from', None)
        metaclass = getattr(stub, 'metaclass', None)

        attrstr = ''
        attrs = []
        if bases:
            if isinstance(bases, str):
                bases = [bases]
            attrs.extend(bases)
        if metaclass:
            metaclassstr = "metaclass={}".format(metaclass)
            attrs.append(metaclassstr)
        if attrs:
            attrstr = attrtmpl.format(attrs=', '.join(attrs))

        clsstr = clstmpl.format(
            clsname=stub.name,
            clsattrs=attrstr,
            indent=" "*4
        )
        return clsstr

    @classmethod
    def gen(cls, stub):
        if not stub:
            return None

        return getattr(cls, '_{}_gen'.format(stub.type))(stub)