# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Players(models.Model):
    aname = models.CharField(db_column='ANAME', primary_key=True, max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    yrstart = models.IntegerField(db_column='YrStart', blank=True, null=True)  # Field name made lowercase.
    yrend = models.IntegerField(db_column='YrEnd', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ht = models.IntegerField(db_column='Ht', blank=True, null=True)  # Field name made lowercase.
    wt = models.IntegerField(db_column='Wt', blank=True, null=True)  # Field name made lowercase.
    birthdata = models.DateField(db_column='BirthData', blank=True, null=True)  # Field name made lowercase.
    colleges = models.CharField(db_column='Colleges', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Players'


class Pergame2014(models.Model):
    pid = models.ForeignKey('Players', models.DO_NOTHING, db_column='PID', unique=True, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg_pct = models.FloatField(db_column='FG_PCT', blank=True, null=True)  # Field name made lowercase.
    fg3m = models.FloatField(db_column='FG3M', blank=True, null=True)  # Field name made lowercase.
    fg3a = models.FloatField(db_column='FG3A', blank=True, null=True)  # Field name made lowercase.
    fg3_pct = models.FloatField(db_column='FG3_PCT', blank=True, null=True)  # Field name made lowercase.
    fg2m = models.FloatField(db_column='FG2M', blank=True, null=True)  # Field name made lowercase.
    fg2a = models.FloatField(db_column='FG2A', blank=True, null=True)  # Field name made lowercase.
    fg2_pct = models.FloatField(db_column='FG2_PCT', blank=True, null=True)  # Field name made lowercase.
    efg = models.FloatField(db_column='EFG', blank=True, null=True)  # Field name made lowercase.
    ftm = models.FloatField(db_column='FTM', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ft_pct = models.FloatField(db_column='FT_PCT', blank=True, null=True)  # Field name made lowercase.
    oreb = models.FloatField(db_column='OREB', blank=True, null=True)  # Field name made lowercase.
    dreb = models.FloatField(db_column='DREB', blank=True, null=True)  # Field name made lowercase.
    reb = models.FloatField(db_column='REB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerGame2014'


class Pergame2015(models.Model):
    pid = models.ForeignKey('Players', models.DO_NOTHING, db_column='PID', unique=True, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg_pct = models.FloatField(db_column='FG_PCT', blank=True, null=True)  # Field name made lowercase.
    fg3m = models.FloatField(db_column='FG3M', blank=True, null=True)  # Field name made lowercase.
    fg3a = models.FloatField(db_column='FG3A', blank=True, null=True)  # Field name made lowercase.
    fg3_pct = models.FloatField(db_column='FG3_PCT', blank=True, null=True)  # Field name made lowercase.
    fg2m = models.FloatField(db_column='FG2M', blank=True, null=True)  # Field name made lowercase.
    fg2a = models.FloatField(db_column='FG2A', blank=True, null=True)  # Field name made lowercase.
    fg2_pct = models.FloatField(db_column='FG2_PCT', blank=True, null=True)  # Field name made lowercase.
    efg = models.FloatField(db_column='EFG', blank=True, null=True)  # Field name made lowercase.
    ftm = models.FloatField(db_column='FTM', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ft_pct = models.FloatField(db_column='FT_PCT', blank=True, null=True)  # Field name made lowercase.
    oreb = models.FloatField(db_column='OREB', blank=True, null=True)  # Field name made lowercase.
    dreb = models.FloatField(db_column='DREB', blank=True, null=True)  # Field name made lowercase.
    reb = models.FloatField(db_column='REB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerGame2015'


class Pergame2016(models.Model):
    pid = models.ForeignKey('Players', models.DO_NOTHING, db_column='PID', unique=True, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg_pct = models.FloatField(db_column='FG_PCT', blank=True, null=True)  # Field name made lowercase.
    fg3m = models.FloatField(db_column='FG3M', blank=True, null=True)  # Field name made lowercase.
    fg3a = models.FloatField(db_column='FG3A', blank=True, null=True)  # Field name made lowercase.
    fg3_pct = models.FloatField(db_column='FG3_PCT', blank=True, null=True)  # Field name made lowercase.
    fg2m = models.FloatField(db_column='FG2M', blank=True, null=True)  # Field name made lowercase.
    fg2a = models.FloatField(db_column='FG2A', blank=True, null=True)  # Field name made lowercase.
    fg2_pct = models.FloatField(db_column='FG2_PCT', blank=True, null=True)  # Field name made lowercase.
    efg = models.FloatField(db_column='EFG', blank=True, null=True)  # Field name made lowercase.
    ftm = models.FloatField(db_column='FTM', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ft_pct = models.FloatField(db_column='FT_PCT', blank=True, null=True)  # Field name made lowercase.
    oreb = models.FloatField(db_column='OREB', blank=True, null=True)  # Field name made lowercase.
    dreb = models.FloatField(db_column='DREB', blank=True, null=True)  # Field name made lowercase.
    reb = models.FloatField(db_column='REB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerGame2016'


class Pergame2017(models.Model):
    pid = models.ForeignKey('Players', models.DO_NOTHING, db_column='PID', unique=True, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg_pct = models.FloatField(db_column='FG_PCT', blank=True, null=True)  # Field name made lowercase.
    fg3m = models.FloatField(db_column='FG3M', blank=True, null=True)  # Field name made lowercase.
    fg3a = models.FloatField(db_column='FG3A', blank=True, null=True)  # Field name made lowercase.
    fg3_pct = models.FloatField(db_column='FG3_PCT', blank=True, null=True)  # Field name made lowercase.
    fg2m = models.FloatField(db_column='FG2M', blank=True, null=True)  # Field name made lowercase.
    fg2a = models.FloatField(db_column='FG2A', blank=True, null=True)  # Field name made lowercase.
    fg2_pct = models.FloatField(db_column='FG2_PCT', blank=True, null=True)  # Field name made lowercase.
    efg = models.FloatField(db_column='EFG', blank=True, null=True)  # Field name made lowercase.
    ftm = models.FloatField(db_column='FTM', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ft_pct = models.FloatField(db_column='FT_PCT', blank=True, null=True)  # Field name made lowercase.
    oreb = models.FloatField(db_column='OREB', blank=True, null=True)  # Field name made lowercase.
    dreb = models.FloatField(db_column='DREB', blank=True, null=True)  # Field name made lowercase.
    reb = models.FloatField(db_column='REB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerGame2017'


class Pergame2018(models.Model):
    pid = models.ForeignKey('Players', models.DO_NOTHING, db_column='PID', unique=True, blank=True, null=False, primary_key=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg_pct = models.FloatField(db_column='FG_PCT', blank=True, null=True)  # Field name made lowercase.
    fg3m = models.FloatField(db_column='FG3M', blank=True, null=True)  # Field name made lowercase.
    fg3a = models.FloatField(db_column='FG3A', blank=True, null=True)  # Field name made lowercase.
    fg3_pct = models.FloatField(db_column='FG3_PCT', blank=True, null=True)  # Field name made lowercase.
    fg2m = models.FloatField(db_column='FG2M', blank=True, null=True)  # Field name made lowercase.
    fg2a = models.FloatField(db_column='FG2A', blank=True, null=True)  # Field name made lowercase.
    fg2_pct = models.FloatField(db_column='FG2_PCT', blank=True, null=True)  # Field name made lowercase.
    efg = models.FloatField(db_column='EFG', blank=True, null=True)  # Field name made lowercase.
    ftm = models.FloatField(db_column='FTM', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ft_pct = models.FloatField(db_column='FT_PCT', blank=True, null=True)  # Field name made lowercase.
    oreb = models.FloatField(db_column='OREB', blank=True, null=True)  # Field name made lowercase.
    dreb = models.FloatField(db_column='DREB', blank=True, null=True)  # Field name made lowercase.
    reb = models.FloatField(db_column='REB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerGame2018'


class Playerid(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlayerId'
