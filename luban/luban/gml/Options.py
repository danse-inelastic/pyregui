

from pyre.inventory.Inventory import Inventory

class Options(Inventory):

    import pyre.inventory

    author = pyre.inventory.str("author", default="")
    organization = pyre.inventory.str("organization", default="")
    copyright = pyre.inventory.str("copyright", default="")

    bannerWidth = pyre.inventory.int("bannerWidth", default=78)
    bannerCharacter = pyre.inventory.str("bannerCharacter", default='~')

    creator = pyre.inventory.str("creator")
    timestamp = pyre.inventory.bool("timestamp", default=True)

    lastLine = pyre.inventory.str("lastLine", default=" End of file ")
    copyrightLine = pyre.inventory.str(
        "copyrightLine", default="(C) %s  All Rights Reserved")
    licenseText = pyre.inventory.preformatted("licenseText", default=["{LicenseText}"])

    timestampLine = pyre.inventory.str(
        "timestampLine", default=" Generated automatically by %s on %s")

    versionId = pyre.inventory.str("versionId", default=' $' + 'Id' + '$')
    
    pass # end of Options
