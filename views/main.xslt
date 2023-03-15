<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>My First XSLT</title>
            </head>
            <body>
                <h1>My First XSLT</h1>
                <xsl:apply-templates select="root"/>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="root">
        <xsl:apply-templates select="child"/>
    </xsl:template>
    <xsl:template match="child">
        <xsl:apply-templates select="grandchild"/>
    </xsl:template>
    <xsl:template match="grandchild">
        <xsl:value-of select="."/>
    </xsl:template>

</xsl:stylesheet>