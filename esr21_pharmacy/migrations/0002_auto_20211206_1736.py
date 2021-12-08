# Generated by Django 3.1.4 on 2021-12-06 15:36

from django.db import migrations, models
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('esr21_pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugaccountabilitylog',
            options={'verbose_name': 'Drug Accountability', 'verbose_name_plural': 'Drug Accountability'},
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='investigator',
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='package_size',
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='storage_temp',
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='study_name',
        ),
        migrations.RemoveField(
            model_name='drugaccountabilitylog',
            name='study_product_name',
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='balance_forward',
            field=models.IntegerField(blank=True, null=True, verbose_name='Balance forward'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='date',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='details',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='received_or_issued',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity received or issues'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='requisition_form_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Requisition form number'),
        ),
        migrations.AddField(
            model_name='drugaccountabilitylog',
            name='status',
            field=models.IntegerField(blank=True, null=True, verbose_name='Status (Active/Quarantined/Disposed)'),
        ),
        migrations.AlterField(
            model_name='drugaccountabilitylog',
            name='exp_date',
            field=models.DateTimeField(default='', verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='drugaccountabilitylog',
            name='site',
            field=models.CharField(blank=True, max_length=25, verbose_name='Injection site name'),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='designation',
            field=models.CharField(choices=[('Indicator Manager/ Destruction monitor', 'Indicator Manager/ Destruction monitor'), ('Pharmacy personnel at BHP', 'Pharmacy personnel at BHP'), ('Pharmacy Personnel at study site', 'Pharmacy Personnel at study site')], max_length=50, verbose_name='Designation'),
        ),
        migrations.DeleteModel(
            name='DrugAccountabilityLogInline',
        ),
    ]