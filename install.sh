cd ./pdfkit
echo "Installing.. pdfkit"
if sudo python setup.py install
then
    echo "Done!"
else
    echo "Error in running script ./pdfkit/setup.py"
    echo "Run it mannualy '$ sudo python setup.py install'"
fi
echo "Installing dependencies..!"
if sudo apt-get install python-gtk2
then
    echo "Done!"
else
    echo "Error in installation!"
fi
if sudo apt-get install python-webkit
then
    echo "Done!"
else
    echo "Error in installation!"
fi
if sudo apt-get install wkhtmltopdf
then
    echo "Done!"
else
    echo "Error in installation!"
fi

