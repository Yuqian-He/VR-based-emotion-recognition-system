// Fill out your copyright notice in the Description page of Project Settings.


#include "readFile.h"
#include "Misc/FileHelper.h"
#include "Misc/Paths.h"

bool UreadFile::LoadTxt(FString FileNameA, FString& SaveTextA)
{
    return FFileHelper::LoadFileToString(SaveTextA, *(FPaths::ProjectDir() + FileNameA));
}

bool UreadFile::SaveTxt(FString SaveTextB, FString FileNameB)
{
    return FFileHelper::SaveStringToFile(SaveTextB, *(FPaths::ProjectDir() + FileNameB));
}