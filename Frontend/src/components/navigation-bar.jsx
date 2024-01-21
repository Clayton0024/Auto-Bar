"use client"
import React from "react"

import {
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuIndicator,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
    NavigationMenuViewport,
  } from "@/components/ui/navigation-menu"
import { navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"
import { NavLink } from "react-router-dom"


export function NavigationBar() {

    return (

    <NavigationMenu>
        <NavigationMenuList>
        <NavigationMenuItem>
                <NavigationMenuLink asChild>
                    <a href="/#/">Home</a>
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink asChild>
                    <a href="/#/settings">Settings</a>
                </NavigationMenuLink>
            </NavigationMenuItem>
        </NavigationMenuList>
    </NavigationMenu>

    )
}