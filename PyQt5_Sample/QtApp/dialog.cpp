#include "dialog.h"
#include "./ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}


void Dialog::on_btnClear_clicked()
{
    ui->textEdit->clear();
}

void Dialog::on_chkBoxUnder_toggled(bool checked)
{
    QFont font = ui->textEdit->font();
    font.setUnderline(checked);
    ui->textEdit->setFont(font);
}

void Dialog::on_chkBoxBold_toggled(bool checked)
{
    QFont font = ui->textEdit->font();
    font.setBold(checked);
    ui->textEdit->setFont(font);
}

void Dialog::on_chkBoxItelic_clicked(bool checked)
{
    QFont font = ui->textEdit->font();
    font.setItalic(checked);
    ui->textEdit->setFont(font);
}
