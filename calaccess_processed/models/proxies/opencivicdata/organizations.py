#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proxy models for augmenting our source data tables with methods useful for processing.
"""
from __future__ import unicode_literals
from django.db import models
from opencivicdata.core.models import (
    Membership,
    Organization,
    OrganizationIdentifier,
    OrganizationName,
)
from .base import OCDProxyModelMixin


class OCDOrganizationManager(models.Manager):
    """
    Custom helpers for the OCD Organization model.
    """
    def senate(self):
        """
        Returns state senate organization.
        """
        return self.get_queryset().get_or_create(
            name='California State Senate',
            classification='upper',
        )[0]

    def assembly(self):
        """
        Returns state assembly organization.
        """
        return self.get_queryset().get_or_create(
            name='California State Assembly',
            classification='lower',
        )[0]

    def executive_branch(self):
        """
        Returns executive branch organization.
        """
        return self.get_queryset().get_or_create(
            name='California State Executive Branch',
            classification='executive',
        )[0]

    def secretary_of_state(self):
        """
        Returns secretary of state organization.
        """
        return self.get_queryset().get_or_create(
            name='California Secretary of State',
            classification='executive',
            parent=self.executive_branch(),
        )[0]

    def elections_division(self):
        """
        Returns the elections division of the secretary of state organization.
        """
        return self.get_queryset().get_or_create(
            name='Elections Division',
            classification='executive',
            parent=self.secretary_of_state(),
        )[0]

    def board_of_equalization(self):
        """
        Returns board of equalization organization.
        """
        return self.get_queryset().get_or_create(
            name='State Board of Equalization',
            parent=self.executive_branch(),
        )[0]


class OCDOrganizationProxy(Organization, OCDProxyModelMixin):
    """
    A proxy on the OCD Organization model with helper methods.
    """
    objects = OCDOrganizationManager()

    class Meta:
        """
        Make this a proxy model.
        """
        proxy = True

    @property
    def doc(self):
        """
        Returns the preferred description for the proxied model.
        """
        return "A group of people, typically in a legislative or rule-making context."


class OCDOrganizationIdentifierProxy(OrganizationIdentifier, OCDProxyModelMixin):
    """
    A proxy on the OCD OrganizationIdentifier model with helper methods.
    """

    class Meta:
        """
        Make this a proxy model.
        """
        proxy = True

    @property
    def doc(self):
        """
        Returns the preferred description for the proxied model.
        """
        return "Upstream identifiers of the organization, if any exist."


class OCDOrganizationNameProxy(OrganizationName, OCDProxyModelMixin):
    """
    A proxy on the OCD OrganizationName model with helper methods.
    """

    class Meta:
        """
        Make this a proxy model.
        """
        proxy = True

    @property
    def doc(self):
        """
        Returns the preferred description for the proxied model.
        """
        return "Alternate or former names for the organization."


class OCDMembershipProxy(Membership, OCDProxyModelMixin):
    """
    A proxy on the OCD Membership model with helper methods.
    """

    class Meta:
        """
        Make this a proxy model.
        """
        proxy = True

    @property
    def doc(self):
        """
        Returns the preferred description for the proxied model.
        """
        return "A relationship between a Person and an Organization, possibly \
including a Post."
