<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>Lottery</title>
                <xml-stylesheet type="text/css" href="../styles/style.css"/>
            </head>
            <body>
                <xsl:apply-templates select="lottery_ui"/>
                <div class="grid_template">
                    <xsl:for-each select="lottery_ui/numbers_slot_1/number">
                        <div class="number">
                            <xsl:value-of select="number"/>
                        </div>
                    </xsl:for-each>
                    <xsl:for-each select="lottery_ui/numbers_slot_2/number">
                        <div class="number">
                            <xsl:value-of select="number"/>
                        </div>
                    </xsl:for-each>
                    <xsl:for-each select="lottery_ui/numbers_slot_3/number">
                        <div class="number">
                            <xsl:value-of select="number"/>
                        </div>
                    </xsl:for-each>
                </div>
            </body>
        </html>
    </xsl:template>
    </xsl:stylesheet>